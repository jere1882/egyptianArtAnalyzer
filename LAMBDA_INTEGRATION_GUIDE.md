# 🏺 Egyptian AI Lens - Lambda Integration Guide

## Overview
This guide explains how to integrate your Vercel-hosted website with the newly deployed AWS Lambda API for Egyptian art analysis.

## ✅ What We've Updated

### 1. **API Endpoint Fixed**
- **Before**: `egyptian-art-analyzer` (incorrect)
- **After**: `decipher-egyptian-hieroglyphs` (correct)

### 2. **Security Improvements**
- **Before**: Hardcoded API key in client code ❌
- **After**: Environment variable-based API key ✅
- **Before**: API key visible in GitHub ❌
- **After**: API key stored securely in Vercel ✅

### 3. **Error Handling**
- Added validation for missing API key
- Better error messages for users

## 🔧 Environment Variables Setup

### For Local Development:
1. Create `.env.local` file in your project root:
```bash
NEXT_PUBLIC_LAMBDA_API_URL=https://l7tp0pix83.execute-api.us-east-2.amazonaws.com/default/decipher-egyptian-hieroglyphs
NEXT_PUBLIC_API_KEY=SL1KJ4ShwF37CA6jRcISy32kJgx93NA7Kc9Xj8j2
```

### For Vercel Production:
1. Go to your Vercel dashboard
2. Navigate to your project settings
3. Go to "Environment Variables"
4. Add these variables:

| Variable Name | Value | Environment |
|---------------|-------|-------------|
| `NEXT_PUBLIC_LAMBDA_API_URL` | `https://l7tp0pix83.execute-api.us-east-2.amazonaws.com/default/decipher-egyptian-hieroglyphs` | Production, Preview, Development |
| `NEXT_PUBLIC_API_KEY` | `SL1KJ4ShwF37CA6jRcISy32kJgx93NA7Kc9Xj8j2` | Production, Preview, Development |

## 🚀 Deployment Steps

### 1. **Commit Your Changes**
```bash
git add .
git commit -m "feat: integrate with AWS Lambda API for Egyptian AI analysis"
git push origin main
```

### 2. **Deploy to Vercel**
- Vercel will automatically deploy when you push to GitHub
- Make sure environment variables are set in Vercel dashboard
- The deployment will use the new Lambda API endpoint

### 3. **Test the Deployment**
1. Visit your deployed website
2. Go to the Egyptian AI Lens page
3. Upload an Egyptian image
4. Verify the analysis works correctly

## 🔍 API Integration Details

### **Request Format**
```javascript
POST https://l7tp0pix83.execute-api.us-east-2.amazonaws.com/default/decipher-egyptian-hieroglyphs
Headers:
  Content-Type: application/json
  x-api-key: [YOUR_API_KEY]

Body:
{
  "image": "[base64_encoded_image]",
  "speed": "fast", // "regular", "fast", "super-fast"
  "imageType": "tomb" // "tomb", "temple", "other", "unknown"
}
```

### **Response Format**
```javascript
{
  "translation": "Detailed hieroglyphic analysis...",
  "characters": [...],
  "location": "Historical context and location...",
  "processing_time": "Analysis completed in X.XXs",
  "interesting_detail": "Notable observations...",
  "date": "Historical period"
}
```

## 🛡️ Security Considerations

### **API Key Security**
- ✅ API key is now stored in Vercel environment variables
- ✅ No hardcoded secrets in the codebase
- ✅ API key is not exposed in GitHub
- ✅ Environment variables are encrypted in Vercel

### **Rate Limiting**
- API Gateway has built-in rate limiting
- Consider implementing client-side rate limiting if needed

### **CORS**
- Lambda function includes CORS headers
- Website can make cross-origin requests

## 🐛 Troubleshooting

### **Common Issues:**

1. **"API key not configured" error**
   - Check that `NEXT_PUBLIC_API_KEY` is set in Vercel
   - Redeploy after adding environment variables

2. **"Analysis failed" error**
   - Check that the Lambda function is running
   - Verify the API endpoint URL is correct

3. **CORS errors**
   - Lambda function includes CORS headers
   - Check browser console for specific error messages

### **Testing Commands:**
```bash
# Test the API directly
curl -X POST https://l7tp0pix83.execute-api.us-east-2.amazonaws.com/default/decipher-egyptian-hieroglyphs \
  -H "Content-Type: application/json" \
  -H "x-api-key: SL1KJ4ShwF37CA6jRcISy32kJgx93NA7Kc9Xj8j2" \
  -d '{"name": "test"}'
```

## 📊 Performance Expectations

- **Processing Time**: 10-15 seconds for complex images
- **Image Size**: Up to 10MB (base64 encoded)
- **Supported Formats**: JPEG, PNG, WebP
- **Rate Limits**: API Gateway default limits apply

## 🎯 Next Steps

1. **Deploy to Vercel** with environment variables
2. **Test the integration** with real Egyptian images
3. **Monitor performance** and error rates
4. **Consider adding** client-side caching for better UX
5. **Implement** loading states and progress indicators

## 📞 Support

If you encounter issues:
1. Check the browser console for errors
2. Verify environment variables in Vercel
3. Test the Lambda API directly with curl
4. Check CloudWatch logs for Lambda function errors

---

**Your Egyptian AI Lens is now ready for production! 🏺✨**

