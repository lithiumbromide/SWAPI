---
title: "GetPartBox Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetPartBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPartBox.html"
---

# GetPartBox Method (IPartDoc)

Gets the box enclosing the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartBox( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Object

value = instance.GetPartBox(NoConversion)
```

### C#

```csharp
System.object GetPartBox(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.Object^ GetPartBox(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`: Convert to user units or not; true retains system units, false changes to user units

### Return Value

Array of 6 doubles containing the 2 diagonal points that bound the part

## VBA Syntax

See [PartDoc::GetPartBox](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetPartBox.html).

## Examples

[Get Part Bounding Box (VBA)](Get_Part_Bounding_Box_Example_VB.htm)

## Remarks

The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

The X,Y,Z points returned are the lower- and upper-diagonal corners that bound the part with the box sides parallel to the X, Y and Z axes. The box dimensions returned enclose the part and usually close to the minimum possible size, but this is not guaranteed.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IComponent2::GetBox Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
