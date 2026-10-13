---
title: "SetName Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetName.html"
---

# SetName Method (IDetailCircle)

Sets the name of this detail circle, as displayed in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetName(Name)
```

### C#

```csharp
System.bool SetName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of this detail circle

### Return Value

True if setting the detail circle name is successful, false if not

## VBA Syntax

See [DetailCircle::SetName](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetName.html).

## Remarks

If setting the name of a feature, then the new name must be unique in the FeatureManager design tree. If the name is not unique, then the name is not changed. Also, the name cannot contain any of the SOLIDWORKS reserved special characters.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetName.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
