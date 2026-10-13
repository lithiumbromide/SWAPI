---
title: "EnableFileMenu Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "EnableFileMenu"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableFileMenu.html"
---

# EnableFileMenu Property (ISldWorks)

Gets or sets whether to enable file-related menus and toolbars.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFileMenu As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

instance.EnableFileMenu = value

value = instance.EnableFileMenu
```

### C#

```csharp
System.bool EnableFileMenu {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableFileMenu {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable file-related menus and toolbars (e.g., open a document, create a new document, open a recent document, etc.,); false to disable file-related menus and toolbars

## VBA Syntax

See [SldWorks::EnableFileMenu](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~EnableFileMenu.html).

## Examples

**Visual Basic for Applications (VBA)**

Option Explicit

Dim swApp As SldWorks.SldWorks
Sub main()

Set swApp = Application.SldWorks

' Disable file-related menus and toolbars
swApp.**EnableFileMenu** = False

' Enable file-related menus and toolbars

swApp.**EnableFileMenu** = True

End Sub

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IModelDoc2::Toolbars](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Toolbars.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
