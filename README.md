# Egyptian Art Analyzer

**AI-powered analysis of ancient Egyptian art, hieroglyphs, and historical artifacts using Google Gemini.**

Upload a photo of Egyptian tomb paintings, temple reliefs, or hieroglyphic inscriptions, and get instant expert-level analysis including:

- **Hieroglyph Translation** - Decode ancient Egyptian text and symbols
- **Character Identification** - Recognize gods, pharaohs, and historical figures by their iconography
- **Location Detection** - Identify famous sites like the Valley of the Kings, Karnak Temple, and specific tombs
- **Historical Context** - Date artifacts to specific Egyptian periods (Old Kingdom, New Kingdom, etc.)
- **Expert Insights** - Discover fascinating details that casual observers might miss

This project leverages Google's Gemini AI to provide Egyptologist-level analysis of ancient Egyptian artwork, making archaeological expertise accessible to tourists, students, and enthusiasts. The API is deployed as a serverless AWS Lambda function for scalability and reliability.

## Project Structure

```
egyptianArtAnalyzer/
├── src/                    # Source code
│   ├── __init__.py
│   ├── lambda_function.py  # AWS Lambda handler
│   ├── gemini_strategy.py  # Gemini AI integration
│   └── schemas.py          # Pydantic data models
├── scripts/                # Deployment scripts
│   ├── deploy.sh          # Main deployment script
│   └── setup-iam.sh       # IAM setup
├── data/                   # Sample Egyptian art images
│   └── README.md
├── predict.py              # Local testing script
├── Dockerfile              # Lambda container definition
├── requirements.txt        # Python dependencies
├── env.example             # Environment variables template
└── README.md               # This file
```

## Getting Started

### Quick Start (Local Testing)

1. **Clone the repository**
```bash
git clone <repo-url>
cd egyptianArtAnalyzer
```

2. **Install the package**
```bash
pip install -e .
```

This installs the package in editable mode along with all dependencies.

3. **Set up your API key**

Copy `env.example` to `env.local` and add your Google API key:
```bash
cp env.example env.local
# Edit env.local and add your GOOGLE_API_KEY
```

Or create `env.local` with:
```bash
echo "GOOGLE_API_KEY=your-key-here" > env.local
```

4. **Test on sample images**
```bash
python predict.py data/sample-egyptian-images/VoK.jpg
```

That's it! The script will analyze the image and display the results.

### Command Options

```bash
# Different speed settings
python predict.py path/to/image.jpg --speed regular    # More accurate, slower
python predict.py path/to/image.jpg --speed fast       # Default, balanced
python predict.py path/to/image.jpg --speed super-fast # Fastest

# Provide image type hints for better analysis
python predict.py path/to/image.jpg --type tomb
python predict.py path/to/image.jpg --type temple

# Get raw JSON output
python predict.py path/to/image.jpg --json
```

## AWS Deployment

### Prerequisites

1. **AWS CLI configured** with appropriate permissions
2. **Docker** installed and running
3. **Google API Key** for Gemini AI (already set up above)
4. **IAM Role** with Lambda execution permissions

### Deployment Steps

1. **Create IAM Role**

Create an IAM role with the following policies:
- `AWSLambdaBasicExecutionRole`
- `AWSLambdaVPCAccessExecutionRole` (if needed)

2. **Deploy to AWS Lambda**

```bash
./scripts/deploy.sh
```

## API Usage

The Lambda function expects a JSON POST request with the following structure:

```json
{
  "image": "base64-encoded-image-data",
  "speed": "fast", // optional: "fast", "regular", "super-fast"
  "imageType": "unknown" // optional: "tomb", "temple", "other", "unknown"
}
```

### Example Request

```bash
curl -X POST https://your-api-gateway-url/egyptian-art-analyzer \
  -H "Content-Type: application/json" \
  -d '{
    "image": "iVBORw0KGgoAAAANSUhEUgAA...",
    "speed": "fast",
    "imageType": "tomb"
  }'
```

### Response Format

```json
{
  "translation": "Ancient text translation...",
  "characters": [
    {
      "character_name": "Osiris",
      "reasoning": "Identified by characteristic crown and staff",
      "description": "God of the afterlife",
      "location": "center of the image"
    }
  ],
  "location": "Valley of the Kings, Tomb of Tutankhamun",
  "processing_time": "Analysis completed in 2.34s",
  "interesting_detail": "The hieroglyphs show the royal cartouche...",
  "date": "New Kingdom"
}
```

## Configuration

- **Timeout**: 30 seconds
- **Memory**: 512 MB
- **Runtime**: Python 3.11
- **Architecture**: x86_64

## Troubleshooting

1. **Check CloudWatch Logs** for detailed error messages
2. **Verify API Gateway** is configured to pass through the request body
3. **Ensure CORS** is properly configured if calling from a web browser
4. **Check IAM permissions** for the Lambda execution role

## Local Testing

You can test the function locally using the AWS SAM CLI or by running the Docker container directly:

```bash
docker build -t egyptian-art-analyzer .
docker run -p 9000:8080 -e GOOGLE_API_KEY=your-key egyptian-art-analyzer
```

Then test with:

```bash
curl -X POST http://localhost:9000/2015-03-31/functions/function/invocations \
  -d '{"httpMethod": "POST", "body": "{\"image\": \"test\"}"}'
```
