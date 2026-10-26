# Image Resizer

A serverless web app that resizes images in seconds. Upload an image, set the width, height and format, and download the result. The resizing runs on **AWS Lambda** using Python and Pillow, and every change is tested and deployed automatically with **GitHub Actions**.


![Deploy](https://dmahi30.github.io/image-resizer/)

## Features

- Upload an image (JPG, PNG, WEBP)
- Set custom width and height (aspect ratio is preserved)
- Convert output to JPEG, PNG or WEBP
- Instant preview and one-click download
- No server and no database to manage
- Automated test and deploy pipeline

## Architecture

```
Browser (HTML/CSS/JS)  ->  Lambda Function URL  ->  AWS Lambda (Python + Pillow)  ->  Resized image
```

The browser sends the image as base64 in a JSON request. The Lambda function resizes it and returns the result as base64.

## Tech Stack

| Technology | Purpose |
|---|---|
| HTML, CSS, JavaScript | Frontend |
| Python 3.12 + Pillow | Image processing |
| AWS Lambda + Function URL | Serverless backend and endpoint |
| pytest | Unit testing |
| Git + GitHub | Version control |
| GitHub Actions | CI/CD |
| Jira | Agile planning (epics, stories, sprints) |

## Project Structure

```
image-resizer/
├── lambda_function.py        # Lambda handler that resizes the image
├── test_lambda.py            # Unit test
├── index.html                # Frontend page
├── .github/workflows/
│   └── deploy.yml            # CI/CD pipeline
├── .gitignore
└── README.md
```

## Run Locally

1. Clone the repo and open it in VS Code:
   ```
   git clone https://github.com/YOUR_USERNAME/image-resizer.git
   cd image-resizer
   ```
2. Install dependencies and run the tests:
   ```
   pip install pillow pytest
   pytest
   ```
3. Open `index.html` in your browser (the Function URL must be set, see below).

## Deploy to AWS

1. Build the Pillow layer (Python 3.12, x86_64):
   ```
   pip install pillow --platform manylinux2014_x86_64 --target python --only-binary=:all: --python-version 3.12
   ```
   Zip the `python` folder as `pillow-layer.zip` and upload it as a Lambda layer.
2. Create a Lambda function named `image-resizer` (Python 3.12), paste in `lambda_function.py`, and attach the layer.
3. Set memory to 512 MB and timeout to 15 seconds.
4. Enable a **Function URL** with auth type `NONE` and configure CORS (origin `*`, method `POST`, header `content-type`).
5. Paste the Function URL into `index.html` where it says `PASTE_YOUR_FUNCTION_URL_HERE`.

## CI/CD Pipeline

The app is deployed through GitHub Actions. There is no manual upload: every push to `main` that passes the tests is released to AWS Lambda automatically. You can see each run under the **Actions** tab of the repo.

On every push to `main`, GitHub Actions:

1. Installs dependencies
2. Runs `pytest`
3. Zips `lambda_function.py`
4. Updates the Lambda function code

Add these secrets under **Settings > Secrets and variables > Actions**:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

Use a limited IAM user that can only update this one function. Never commit AWS keys to the repo.

## Agile Workflow

Work is tracked in Jira using epics, user stories and two sprints. Commit messages include the Jira ticket key, for example `IMG-4: add format option`.

## Limitations

- Very large images may exceed the Lambda request size limit
- The Function URL is public with no login
- Resized images are not stored

## Future Scope

- Watermarking
- Batch resizing
- Storing images in S3
- Docker and Terraform support
