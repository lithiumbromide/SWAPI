---
title: "SetName Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetName.html"
---

# SetName Method (IAnnotation)

Sets the name of this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal NameIn As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim NameIn As System.String
Dim value As System.Boolean

value = instance.SetName(NameIn)
```

### C#

```csharp
System.bool SetName(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.bool SetName(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: New and unique name for this annotation

### Return Value

True if the name was successfully changed, false if the name was not successfully changed

## VBA Syntax

See [Annotation::SetName](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetName.html).

## Examples

[Get and Set Name of Note (VBA)](Get_and_Set_Names_of_Note_Example_VB.htm)

## Remarks

This method verifies that the name is unique before attempting to set the name.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetName.html)

## Availability

SOLIDWORKS 99, datecode 1999207
