---
title: "ViewDisplayFaceted Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ViewDisplayFaceted"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDisplayFaceted.html"
---

# ViewDisplayFaceted Method (IModelDoc2)

Sets the current display mode to show the facets that make up a shaded picture of STL output.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ViewDisplayFaceted()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.ViewDisplayFaceted()
```

### C#

```csharp
void ViewDisplayFaceted()
```

### C++/CLI

```cpp
void ViewDisplayFaceted();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::ViewDisplayFaceted](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ViewDisplayFaceted.html).

## Examples

Option Explicit

Sub main()

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

swModel.ViewDisplayFaceted

End Sub

## Examples

[Display Hidden Lines (VBA)](Display_Hidden_Lines_Example_VB.htm)
[Display Hidden Lines (VB.NET)](Display_Hidden_Lines_Example_VBNET.htm)
[Display Hidden Lines (C#)](Display_Hidden_Lines_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
