---
title: "SetLabel Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "SetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~SetLabel.html"
---

# SetLabel Method (IProjectionArrow)

Sets the label for this view's projection arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim Label As System.String
Dim value As System.Boolean

value = instance.SetLabel(Label)
```

### C#

```csharp
System.bool SetLabel(
   System.string Label
)
```

### C++/CLI

```cpp
System.bool SetLabel(
   System.String^ Label
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Label`: Label for this projection arrow

### Return Value

True if setting the label is successful, false if not

## VBA Syntax

See [ProjectionArrow::SetLabel](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~SetLabel.html).

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetLabel.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
