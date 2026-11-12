# JavaScript
DraftSight's JavaScript interface runs in a web page: the page loads client libraries from the local DraftSight API service, which relays calls to the running DraftSight. Every shipped JavaScript example is a complete HTML page; print one with `swapi.py example "Insert Shapes Example (JS)"` and adapt it rather than starting from scratch.
## Page skeleton
- Load `djConnect.js` and `dsApplication.js`, then one library per interface the page uses, all from the service: `http://localhost:7776/APISDK/djLibrary/djConnect.js`, `.../dsApplication.js`, `.../dsDocument.js`, `.../dsModel.js`, `.../dsSketchManager.js` and so on (the file name is the interface name with `ds` instead of `I`). A missing library makes calls on that interface fail.
- Connect with `var mScript = new djScriptManager(); var mApp = mScript.getApplication();`, call `mApp.AbortRunningCommand()`, then use the same members as the other languages (`mApp.GetActiveDocument().GetModel().GetSketchManager()`).
- Wrap the code in `try` and report `djErrorString(err)` in the page, as the examples do.
- Call `mApp.releaseAll()` when the page is done, or `dsObject.release()` per object, because the server keeps every object the page touched until it is released and leaks it otherwise.
## Syntax differences
- Properties are accessor calls: `circle.get_Color()`, `entity.put_Color(dsColor)`, `get_Layer()`, `put_Elevation(100)`.
- Enum values are strings with the member name: `"dsNamedColor_Red"`, `"dsZoomRange_Fit"`; combine bitmask members with semicolons in one string (`"dsHatchBoundaryLoopType_Polyline;dsHatchBoundaryLoopType_Textbox"`).
- A member with one output returns it; a member with several outputs returns an object whose fields are the parameter names from the help (`var c = dsCCS.GetDefaultCustomCoordinateSystemFlag(); c.IsDefault`).
- Arrays are JavaScript arrays.
## Requirements and troubleshooting
- The DraftSight API Service must run. "dsJServerError: jsServer connection Failed" means it is stopped: start DraftSight API Service in services.msc, or run `dsHttpApiController.exe "DraftSight API Service" -s` from `install_dir\bin` as administrator. A port conflict keeps it from starting; the Getting Started topic points to a Dassault Systèmes community tool that changes the port.
- The help names Internet Explorer 8 or later, Firefox and Chrome as supported browsers and advises against Safari; "TypeError: 'JSON' is undefined" means an older Internet Explorer.
- Pages opened from a network share fail with "TypeError: Access is denied"; copy them to a local disk.
- Read the Getting Started topic's JavaScript section for details: `swapi.py topic "Getting Started"`.
