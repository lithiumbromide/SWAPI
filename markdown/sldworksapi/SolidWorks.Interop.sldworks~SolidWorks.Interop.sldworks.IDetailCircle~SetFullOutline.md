---
title: "SetFullOutline Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetFullOutline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetFullOutline.html"
---

# SetFullOutline Method (IDetailCircle)

Sets whether the complete detail circle or detail profile is shown in the detail view, or if just the part of the circle or profile that intersects the view geometry is shown.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFullOutline( _
   ByVal FullOutline As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim FullOutline As System.Boolean
Dim value As System.Boolean

value = instance.SetFullOutline(FullOutline)
```

### C#

```csharp
System.bool SetFullOutline(
   System.bool FullOutline
)
```

### C++/CLI

```cpp
System.bool SetFullOutline(
   System.bool FullOutline
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FullOutline`: True if the full circle or profile outline is shown in the detail view, false if only the portion of the circle or profile that intersects the view geometry is shown

### Return Value

True if setting the full outline flag is successful, false if not

## VBA Syntax

See [DetailCircle::SetFullOutline](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetFullOutline.html).

## Remarks

This method:

- is only available when [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.html) is false.
- automatically loads the model for the detail view if necessary, without prompting the user.

If the style of the detail circle (see [IDetailCircle::GetStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle~GetStyle.html)) is swDetViewCONNECTED, then this method cannot disable the full outline because the full outline of the circle or profile must be shown.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::HasFullOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~HasFullOutline.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
