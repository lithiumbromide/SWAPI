---
title: "IApplication Interface"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IApplication"
member: ""
kind: "interface"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication.html"
---

# IApplication Interface

Provides access to the SOLIDWORKS Toolbox Browser add-in. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IApplication
```

### Visual Basic (Usage)

```vb
Dim instance As IApplication
```

### C#

```csharp
public interface IApplication
```

### C++/CLI

```cpp
public interface class IApplication
```

## VBA Syntax

See [Application](ms-its:toolboxapivb6.chm::/ToolboxBrowser~Application.html).

## Examples

See [Getting Started](GettingStarted-toolboxapi.html) for more information.

## Remarks

This interface is available only if SOLIDWORKS Toolbox Browser add-in is an active SOLIDWORKS add-in.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser_namespace.html) topic for a list of delegates for this interface.

## Accessors

Call [ISldWorks::GetAddInObject](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetAddInObject.html), passing in the GUID of the SOLIDWORKS Toolbox Browser add-in type library (**Registry Editor >** **Computer\HKEY_CLASSES_ROOT\TypeLib\{ED783340-D5DB-11d4-BD5A-00C04F019809}**), to get a Dispatch pointer to the IApplication object and connect to the SOLIDWORKS Toolbox Browser.

For example, in COM:

LPDISPATCH pDisp = NULL;
HRESULT hres = pSldWorks->GetAddInObject("{ED783340-D5DB-11d4-BD5A-00C04F019809}" , &pDisp);

## See Also

[IApplication Members](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication_members.html)
[SolidWorks.Interop.swbrowser Namespace](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser_namespace.html)
