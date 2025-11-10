from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
import controller.user_controller as user_controller

router = APIRouter(prefix='/user',tags=["user"])

@router.post("/login", status_code= 200)
def login_route(email:str=Form(...,description="User email"),
          password: str = Form("...",description="User password")):
        
        """
        Authenticate a user and return a JWT token if credentials are valid.

        This endpoint:
            - Verifies if the provided email exists in the database.
            - Checks if the password matches the stored hash.

        Args:
            email (str): The email of the user (from form data).
            password (str): The password of the user (from form data).

        Returns:
            JSONResponse:
                - 200: Successful login with a JWT token.
                - 401: Invalid email or password.
                - 500: Internal server error.
        """
        try:
            result = user_controller.login(email,password)
            
            print(result)
            
            if result:
                return JSONResponse({'message': 'Yess'}, status_code=200)
            else:
                return JSONResponse({'message': 'E-mail or Password Invalid'}, status_code = 401)
        
        except Exception:
            return JSONResponse({'message': 'Internal Server Error, contact an admin or check console log'}, status_code=500)
        
@router.post("/", status_code= 201)
def register_rotue(name:str = Form (..., description='User name'), 
                   email:str= Form(..., description="User email"),
                   password:str = Form(..., description="User password")):
    """
        Create a new user and return if credentials are valid.

        This endpoint:
            - Verifies if the provided email exists in the database.

        Args:
            email (str): The email of the user (from form data).
            password (str): The password of the user (from form data).

        Returns:
            JSONResponse:
                - 201: Successful create new User.
                - 401: Invalid email or password.
                - 500: Internal server error.
        """
    result = user_controller.register(name,email,password)
    
    if result:
        return JSONResponse({'message': 'Yess'}, status_code=200)
    else:
        return JSONResponse({'message': 'E-mail Invalid or in use'}, status_code = 401)
    
user_router = router #Renomeando para exportar mais facil assim não preciso dar o apelido com 'as' a cada import.