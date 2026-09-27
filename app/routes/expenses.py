from fastapi import APIRouter, Depends, Form
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Expense
from app.services.recommendation_service import generate_budget_recommendation

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("/add")
def add_expense(
    category: str = Form(...),
    amount: float = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db)
):
    expense = Expense(
        user_id=1,
        category=category,
        amount=amount,
        description=description
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return {
        "message": "Expense added successfully",
        "expense_id": expense.id
    }


@router.get("/")
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()

    return expenses
@router.get("/budget")
def get_budget(
    income: float,
    db: Session = Depends(get_db)
):
    expenses = db.query(Expense).all()

    total_expenses = sum(
        expense.amount for expense in expenses
    )

    remaining = income - total_expenses

    return {
        "income": income,
        "total_expenses": total_expenses,
        "remaining_budget": remaining
    }
@router.get("/recommendation")
def budget_recommendation(
    income: float,
    db: Session = Depends(get_db)
):
    expenses = db.query(Expense).all()

    total_expenses = sum(
        expense.amount for expense in expenses
    )

    recommendation = generate_budget_recommendation(
        income,
        total_expenses
    )

    return {
        "income": income,
        "total_expenses": total_expenses,
        "recommendation": recommendation
    }
@router.get("/report")
def generate_report(
    income: float,
    db: Session = Depends(get_db)
):
    expenses = db.query(Expense).all()

    total_expenses = sum(
        expense.amount for expense in expenses
    )

    recommendation = generate_budget_recommendation(
        income,
        total_expenses
    )

    output_path = "pocket_smart_budget_report.docx"

    from app.services.document_service import create_budget_report

    create_budget_report(
         income=income,
          total_expenses=total_expenses,
          recommendation=recommendation,
          expenses=expenses,
           output_path=output_path
)

    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="PocketSmart_Budget_Report.docx"
    )