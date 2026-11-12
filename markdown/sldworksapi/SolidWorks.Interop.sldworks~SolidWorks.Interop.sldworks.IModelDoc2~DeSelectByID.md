---
title: "DeSelectByID Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeSelectByID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeSelectByID.html"
---

# DeSelectByID Method (IModelDoc2)

Removes the selected object from the selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelectByID( _
   ByVal SelID As System.String, _
   ByVal SelParams As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim SelID As System.String
Dim SelParams As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.DeSelectByID(SelID, SelParams, X, Y, Z)
```

### C#

```csharp
System.bool DeSelectByID(
   System.string SelID,
   System.string SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool DeSelectByID(
   System.String^ SelID,
   System.String^ SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelID`: ID of object
- `SelParams`: Type name of object (uppercase)
- `X`: X selection location
- `Y`: Z selection location
- `Z`: Z selection location

### Return Value

True if object is deselected, false otherwise

## VBA Syntax

See [ModelDoc2::DeSelectByID](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeSelectByID.html).

## Examples

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

## Remarks

See [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) for more information about selections.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
