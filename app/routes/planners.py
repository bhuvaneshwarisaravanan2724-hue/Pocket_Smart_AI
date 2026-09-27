from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/planners", tags=["Planners"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/home", response_class=HTMLResponse)
def home_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home_planner.html"
    )
    return """
    <html>
    <head>
        <title>Home Planner - Pocket Smart AI</title>
    </head>

    <body style="font-family: Arial; text-align: center; background: #f4f7fb;">

        <h1 style="background: #1f3c88; color: white; padding: 30px;">
            🏠 Home Planner
        </h1>

        <div style="background: white; max-width: 600px; margin: 50px auto; padding: 35px; border-radius: 18px;">
            <h2>Plan Your Home Needs 🏠</h2>

            <p>
                Plan your home purchases while staying within your budget.
            </p>

            <p>
                💰 Smart planning helps you spend wisely
                and avoid unnecessary expenses.
            </p>

            <a href="/" style="display: inline-block; margin-top: 25px; padding: 10px 18px; background: #1f3c88; color: white; text-decoration: none; border-radius: 8px;">
                ← Back to Home
            </a>
        </div>

    </body>
    </html>
    """
@router.get("/party", response_class=HTMLResponse)
def party_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="party_planner.html"
    )
    return """
    <html>
    <head>
        <title>Party Planner - Pocket Smart AI</title>
    </head>

    <body style="font-family: Arial; text-align: center; background: #f4f7fb;">

        <h1 style="background: #1f3c88; color: white; padding: 30px;">
            🎉 Party Planner
        </h1>

        <div style="background: white; max-width: 600px; margin: 50px auto; padding: 35px; border-radius: 18px;">
            <h2>Plan Your Party 🎉</h2>

            <p>
                Plan your party while staying within your budget.
            </p>

            <p>
                💰 Smart planning helps you control expenses
                and enjoy your event without overspending.
            </p>

            <a href="/" style="display: inline-block; margin-top: 25px; padding: 10px 18px; background: #1f3c88; color: white; text-decoration: none; border-radius: 8px;">
                ← Back to Home
            </a>
        </div>

    </body>
    </html>
    """
@router.get("/jewelry", response_class=HTMLResponse)
def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html"
    )
    return """
    <html>
    <head>
        <title>Jewelry Planner - Pocket Smart AI</title>
    </head>

    <body style="font-family: Arial; text-align: center; background: #f4f7fb;">

        <h1 style="background: #1f3c88; color: white; padding: 30px;">
            💎 Jewelry Planner
        </h1>

        <div style="background: white; max-width: 600px; margin: 50px auto; padding: 35px; border-radius: 18px;">
            <h2>Plan Your Jewelry Purchase 💎</h2>

            <p>
                Find jewelry options while staying within your budget.
            </p>

            <p>
                💰 Smart planning helps you choose wisely
                without overspending.
            </p>

            <a href="/" style="display: inline-block; margin-top: 25px; padding: 10px 18px; background: #1f3c88; color: white; text-decoration: none; border-radius: 8px;">
                ← Back to Home
            </a>
        </div>

    </body>
    </html>
    """