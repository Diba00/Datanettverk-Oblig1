# Datanettverk-Oblig1

<div>
  <h3>📌 Task 1: Making a simple webserver</h3>
  <ul>
    <li>👨‍💻 Develop a web server that handles one HTTP request at a time</li>
    <li>📥 Accept and parse HTTP request, get the requested file, create HTTP response message and send it to the client</li>
    <li>🚫 If requested file not found, send "404 Not Found" message to the client</li>
    <li>📂 Put an HTML file in the server directory and run the server program</li>
    <li>🌐 Open a browser and provide the corresponding URL to display contents of the HTML file</li>
    <li>🆔 Use the port number specified in the server code</li>
  </ul>
  <h3>📌 Task 2: Making a web client</h3>
  <ul>
    <li>👨‍💻 Write own HTTP client to test the server</li>
    <li>🔗 Connect to the server using a TCP connection, send an HTTP request and display server response as output</li>
    <li>⌨️ Command line arguments specify server IP address, host name, port, and path of requested object on server</li>
    <li>📋 Input command format: client.py server host server port filename</li>
  </ul>
  <h3>📌 Task 3: Making a multi-threaded web server</h3>
  <ul>
    <li>👨‍💻 Implement a multithreaded server capable of serving multiple requests simultaneously</li>
    <li>🔗 Use threading to create a main thread for server to listen for clients at a fixed port</li>
    <li>📥 Set up TCP connection through another port and service client request in a separate thread</li>
    <li>🧵 Separate TCP connection and thread for each request/response pair.</li>
  </ul>
</div>
