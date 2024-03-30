## Preferred IDE: Pycharm

### Test the Streamlit app locally:

1. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Streamlit app locally:
    ```bash
    streamlit run app.py
    ```

### Building the Docker image

(Note: Run as administrator on Windows and remove "sudo" in commands)

3. Important - Make sure you have installed Docker on your PC:
   - Linux: Docker
   - Windows/Mac: Docker Desktop

4. Start Docker:
   - Linux (Home Directory):
     ```bash
     sudo systemctl start docker
     ```
   - Windows: Start Docker engine from Docker Desktop.

5. Build Docker image from the project directory:
    ```bash
    sudo docker build -t Image_name:tag .
    ```

### (Note: Rerun the Docker build command if you want to make any changes to the code files and redeploy.)

### Running the container & removing it

6. Switch to Home Directory:
    ```bash
    cd ~
    ```

   List the built Docker images:
    ```bash
    $ sudo docker images
    ```

7. Start a container:
    ```bash
    sudo docker run -p 80:80 Image_ID
    ```

8. This will display the URL to access the Streamlit app (http://0.0.0.0:80). Note that this URL may not work on Windows. For Windows, go to http://localhost/.

9. In a different terminal window, you can check the running containers with:
    ```bash
    sudo docker ps
    ```

10. Stop the container:
    - Use `ctrl + c` or stop it from Docker Desktop.

11. Check all containers:
    ```bash
    sudo docker ps -a
    ```

12. Delete the container if you are not going to run this again:
    ```bash
    sudo docker container prune
    ```

### Pushing the Docker image to Docker Hub

13. Sign up on Docker Hub.

14. Create a repository on Docker Hub.

15. Log in to Docker Hub from the terminal. You can log in with your password or access token.
    ```bash
    sudo docker login
    ```

17. Tag your local Docker image to the Docker Hub repository:
    ```bash
    sudo docker tag Image_ID username/repo-name:tag
    ```

17. Push the local Docker image to the Docker Hub repository:
    ```bash
    sudo docker push username/repo-name:tag
    ```

(If you want to delete the image, you can delete the repository in Docker Hub and force delete it locally.)

18. Command to force delete an image (but don't do this yet):
    ```bash
    sudo docker rmi -f IMAGE_ID
    ```
