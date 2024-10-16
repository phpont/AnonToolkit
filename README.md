# AnonToolkit
===========

AnonToolkit is a tool developed to enhance privacy, anonymity, and security during browsing. This application contains multiple features that allow users to perform actions such as checking their IP, clearing browsing data, changing the MAC address, and more. The graphical interface is built using the Flet library, providing a user-friendly and intuitive interaction.

Features
--------

1.  **Check IP and Geolocation**: Obtains the user's public IP and approximate geographical location (city, region, and country) through the ipinfo.io service.

2.  **Clear Browser Fingerprints**: Removes cache and profile data from Firefox and Chrome browsers to reduce tracking.

3.  **Flush DNS Cache**: Clears the DNS cache to avoid resolution problems and possible tracking.

4.  **Change MAC Address**: Changes the network interface's MAC address, making it harder to track the device by hardware identification.

5.  **Change User-Agent (Placeholder)**: A feature under development to allow changing the browser's User-Agent.

6.  **Check VPN Connection**: Checks whether the current connection is made through a VPN by analyzing the ASN and service provider.

7.  **System Cleanup**: Executes commands to clean the system, removing unnecessary files and freeing up space.

8.  **Clear Cookies**: Clears cookies stored in Firefox and Chrome browsers.

9.  **Disable WebRTC (Firefox)**: Disables WebRTC in Firefox to prevent IP leaks during calls.

10. **Browser Specific Options (Placeholder)**: A feature under development to provide specific options for browsers like Chrome and Firefox.

How to Use
----------

1.  **Installation**: Ensure that Python and the required dependencies are installed. Install the dependencies with the command:

    ```
    pip install flet requests
    ```

2.  **Execution**: To start the tool, run the `main.py` script:

    ```
    python main.py
    ```

3.  **Interface**: The interface displays a panel on the left with buttons that trigger each of the described functionalities. The results of the operations are displayed in the panel on the right.

Current State of the Project
----------------------------

Currently, AnonToolkit provides basic functionalities to improve user privacy and anonymity. Some features are still under development, such as User-Agent switching and specific options for browsers. IP geolocation may not be completely accurate, as it depends on the geolocation provider's database, which may vary in accuracy.

**Known Issues**:

-   IP geolocation may have limited accuracy, especially in rural areas or where internet providers reuse IPs from neighboring regions.

-   Some features, such as changing the MAC address, may not work on Windows systems due to operating system limitations.

Future Goals
------------

1.  **Improving Geolocation Accuracy**: Implement support for using other APIs, such as MaxMind, to increase IP geolocation accuracy.

2.  **User-Agent Switching**: Complete the implementation of the functionality to change the browser's User-Agent, allowing greater customization and anonymity.

3.  **Integration with Other Browsers**: Provide specific options and optimizations for browsers other than Firefox and Chrome, such as Edge and Brave.

4.  **Privacy Task Automation**: Allow users to set up a routine of tasks to be executed automatically (e.g., clearing cookies and flushing DNS daily).

5.  **Interface Improvements**: Make the interface more responsive to different resolutions and improve overall usability.

Contributions
-------------

This project is in its initial phase and is open to contributions. If you have suggestions, find bugs, or would like to help with development, feel free to open issues or pull requests on the GitHub repository.

**GitHub**: [phpont](https://github.com/phpont)

License
-------

This project is available under the MIT license.
