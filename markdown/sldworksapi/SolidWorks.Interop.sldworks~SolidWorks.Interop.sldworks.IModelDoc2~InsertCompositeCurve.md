---
title: "InsertCompositeCurve Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCompositeCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCompositeCurve.html"
---

# InsertCompositeCurve Method (IModelDoc2)

Inserts a composite curve based on selections.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCompositeCurve() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.InsertCompositeCurve()
```

### C#

```csharp
System.bool InsertCompositeCurve()
```

### C++/CLI

```cpp
System.bool InsertCompositeCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertCompositeCurve](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCompositeCurve.html).

## Examples

[Insert a Composite Curve (C#)](Insert_a_Composite_Curve_Example_CSharp.htm)
[Insert a Composite Curve (VB.NET)](Insert_a_Composite_Curve_Example_VBNET.htm)
[Insert a Composite Curve (VBA)](Insert_a_Composite_Curve_Example_VB.htm)

## Remarks

To use this method, select the entities by calling [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark number of 1.

See the SOLIDWORKS Help for information about which entities are valid for selection.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
