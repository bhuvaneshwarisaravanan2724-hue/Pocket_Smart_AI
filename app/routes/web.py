from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.models import Expense
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.recommendation_service import generate_budget_recommendation
router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html"
)
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )
@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )
@router.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )
@router.get("/budget", response_class=HTMLResponse)
def budget_page(
    request: Request,
    db: Session = Depends(get_db)
):
    income = float(request.query_params.get("income", 10000))
    expenses = sum(expense.amount for expense in db.query(Expense).all())
    remaining = income - expenses

    return templates.TemplateResponse(
        request=request,
        name="budget.html",
        context={
            "income": income,
            "expenses": expenses,
            "remaining": remaining
        }
    )
@router.get("/expenses-page", response_class=HTMLResponse)
def expenses_page(
    request: Request,
    db: Session = Depends(get_db)
):
    expenses = db.query(Expense).all()

    return templates.TemplateResponse(
        request=request,
        name="expenses.html",
        context={"expenses": expenses}
    )
@router.get("/recommendation", response_class=HTMLResponse)
def recommendation_page(
    request: Request,
    income: float = 10000,
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

    return templates.TemplateResponse(
        request=request,
        name="recommendation.html",
        context={
            "income": income,
            "expenses": total_expenses,
            "recommendation": recommendation
        }
    )
@router.get("/history", response_class=HTMLResponse)
def history_page(
    request: Request,
    db: Session = Depends(get_db)
):
    expenses = db.query(Expense).all()

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "expenses": expenses,
            "expense_count": len(expenses)
        }
    )