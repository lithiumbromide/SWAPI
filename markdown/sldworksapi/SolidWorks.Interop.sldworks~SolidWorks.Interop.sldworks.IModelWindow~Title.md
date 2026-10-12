---
title: "Title Property (IModelWindow)"
project: "SOLIDWORKS API Help"
interface: "IModelWindow"
member: "Title"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~Title.html"
---

# Title Property (IModelWindow)

Gets the title of this model window.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Title As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelWindow
Dim value As System.String

value = instance.Title
```

### C#

```csharp
System.string Title {get;}
```

### C++/CLI

```cpp
property System.String^ Title {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Title of this model window

## VBA Syntax

See [ModelWindow::Title](ms-its:sldworksapivb6.chm::/sldworks~ModelWindow~Title.html).

## Examples

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## See Also

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
