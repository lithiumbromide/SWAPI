---
title: "IGetPartBox Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetPartBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetPartBox.html"
---

# IGetPartBox Method (IPartDoc)

Gets the box enclosing the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPartBox( _
   ByVal NoConversion As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Double

value = instance.IGetPartBox(NoConversion)
```

### C#

```csharp
System.double IGetPartBox(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.double IGetPartBox(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`: Convert to user units or not; True retains system units, false changes to user units

### Return Value

- in-process, unmanaged C++: Pointer to an array of 6 doubles containing the 2 diagonal points that bound the part
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Return Box Extents (C++)](Return_Box_Extents_Example_CPlusPlus_COM.htm)

## Remarks

The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

The X,Y,Z points returned are the lower- and upper-diagonal corners that bound the part with the box sides parallel to the X, Y and Z axes. The box dimensions returned enclose the part and usually close to the minimum possible size, but this is not guaranteed.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
