Welcome to Pywinauto Element and BaseLayer's documentation!
===========================================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:



Connection to an application
=============================
.. py:function:: connect_to_app(app_name, proc_name, backend='uia')

	Establishes a connection to the target application

	:param app_name: name of the application you wish to run. This can either be the complete path to the application (ex: drive_name\users\username\app_name.exe or just the name of the application, if the app has been added to the environment variables). For reference, in the example the app_name will be “calc.exe”, which launches the windows 10 default calculator.	
    
	:param proc_name: name of the process that is being launched. As an example: the process name of the windows10 default calculator app is simply “Calculator”. Note: You can find this, by checking under Task Manager\Details, and searching for the application that has been spawned.
	
	:param backend: the backend parameter pertains to pywinauto and is used to determine which type of accessibility technology will be used for the tested application. By default it is set to uia. The documentation for this can be found by following this link. It is important to note that the connect_to_app() function is a singleton, as it’s only ever needed to test a single instance of the connection at a time.
	
	:return: Dialog window aka top_window. The pywinauto "root" element used to interact with the application

Element
===================
.. py:method:: __init__(self, application_path, process_name)
	
	The constructor of the method needs two parameters so it will be able to call the connect_to_app() singleton function
	
	:param application_path: name of the application you wish to run. This can either be the complete path to the application
	
	:param process_name: name of the process that is being launched.
	
.. py:method:: ret_window_handle()
	
	:return: Method that returns the window handle (topmost window)

.. py:method:: ret_element(self, locator_strategy=None, locator=None, **kwargs)
	
	A method used to return the sought after element
	
	:param locator_strategy: the locator strategy (auto_id, title, etc) by which an element can be identified. Drawing a comparison to web automation, this would be the equivalent of id, class, partial link text etc. Note: Fastest locator strategies are generally the automation_id (auto_id) strategies
	
	:param locator: value of the locator strategy.
	
	:param kwargs: Not yet implemented
	
	:return: Pywinauto object that is used to interact with the desired element

.. py:method:: click_element(self, locator_strategy, locator)
	
	Clicks the element with the specified locators
	
	:param locator_strategy: the locator strategy (auto_id, title, etc) by which an element can be identified. Drawing a comparison to web automation, this would be the equivalent of id, class, partial link text etc. Note: Fastest locator strategies are generally the automation_id (auto_id) strategies.
	
	:param locator: value of the locator strategy.
	
	:return: Does not return any value, instead it clicks the element.

.. py:method:: get_element_text(self, locator_strategy, locator)

	Returns the text displayed in the window

	:param locator_strategy: the locator strategy (auto_id, title, etc) by which an element can be identified. Drawing a comparison to web automation, this would be the equivalent of id, class, partial link text etc. Note: Fastest locator strategies are generally the automation_id (auto_id) strategies.
	
	:param locator: value of the locator strategy.
	
	:return: a string containing the element’s text. Of note is the fact that the pywinauto method used is .window_text() that returns the text visible to the user from the UI.
	
	:rtype: string
	
	Note: Fastest locator strategies are generally the automation_id (auto_id) strategies.

.. py:method:: send_kb_keys(self, locator_strategy=None, locator=None, keyboard_input=None)

	Sends keys to the topmost window by default. If locator strategies are used then it will send keyboard keys to the desired element

	:param locator_strategy: the locator strategy (auto_id, title, etc) by which an element can be identified. Drawing a comparison to web automation, this would be the equivalent of id, class, partial link text etc. Note: Fastest locator strategies are generally the automation_id (auto_id) strategies.
    
	:param locator: value of the locator strategy.
	
	:param keyboard_input: contains the string of characters to be sent to the application. Note: All arguments are initially set to None, since this way, inputs can be sent directly to the application’s topmost window.

.. py:method:: toggle_element(self, locator_strategy, locator)		

	Get toggle state works for checkboxes as well as for toggles!
    
	:return: toggle state of the element in question

	:rtype: Boolean
	
.. py:method:: maximize_window(self)

	Maximizes the window
		
.. py:method:: close_app(self)

	Closes the application
	
BaseLayer
===================
.. automodule:: pywin_lib
.. autoclass:: BaseLayer
	:members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
