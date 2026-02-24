# OpenAPI Middleware Implementation Challenge

## Overview
In this coding challenge, you will implement middleware for a server that dynamically routes API requests based on an OpenAPI specification document. You'll be expected to set up a project in any language of choice and based on an HTTP client (you may use something like Express/Koa in NodeJS, for example)

### Requirements

Write an HTTP server, create a middleware function that takes in a HTTP request and outputs an HTTP response.
Your middleware should:
1. Match an HTTP request to a route in the OpenAPI spec if it exists.
2. Outputs the corresponding response if the input matches one of the examples in the OpenAPI request.
   1. If the request input doesn't exactly match any examples (by performing a strict comparison), then the server should return a 4xx error, defined in the responses for the endpoint. If no 4xx error is defined, then the server should return a 500 error.
3. Your server should run on localhost:3000

See the `openapi.json` file attached, as a sample spec that you should support.

For the purposes of this question, you only need to handle the same edge cases that you see in the sample `openapi.json` file, but your solution should handle any similar OpenAPI specs regardless of how large this is.

