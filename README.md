# Datanettverk-Oblig1

<div>
  <h3>๐ Task 1: Making a simple webserver</h3>
  <ul>
    <li>๐จโ๐ป Develop a web server that handles one HTTP request at a time</li>
    <li>๐ฅ Accept and parse HTTP request, get the requested file, create HTTP response message and send it to the client</li>
    <li>๐ซ If requested file not found, send "404 Not Found" message to the client</li>
    <li>๐ Put an HTML file in the server directory and run the server program</li>
    <li>๐ Open a browser and provide the corresponding URL to display contents of the HTML file</li>
    <li>๐ Use the port number specified in the server code</li>
  </ul>
  <h3>๐ Task 2: Making a web client</h3>
  <ul>
    <li>๐จโ๐ป Write own HTTP client to test the server</li>
    <li>๐ Connect to the server using a TCP connection, send an HTTP request and display server response as output</li>
    <li>โจ๏ธ Command line arguments specify server IP address, host name, port, and path of requested object on server</li>
    <li>๐ Input command format: client.py server host server port filename</li>
  </ul>
  <h3>๐ Task 3: Making a multi-threaded web server</h3>
  <ul>
    <li>๐จโ๐ป Implement a multithreaded server capable of serving multiple requests simultaneously</li>
    <li>๐ Use threading to create a main thread for server to listen for clients at a fixed port</li>
    <li>๐ฅ Set up TCP connection through another port and service client request in a separate thread</li>
    <li>๐งต Separate TCP connection and thread for each request/response pair.</li>
  </ul>
</div>
