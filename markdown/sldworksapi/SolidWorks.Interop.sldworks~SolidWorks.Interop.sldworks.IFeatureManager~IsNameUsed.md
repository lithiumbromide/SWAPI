---
title: "IsNameUsed Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IsNameUsed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IsNameUsed.html"
---

# IsNameUsed Method (IFeatureManager)

Checks to see whether the specified name is unique in the FeatureManager design tree and valid to use.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsNameUsed( _
   ByVal Type As System.Integer, _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Name As System.String
Dim value As System.Boolean

value = instance.IsNameUsed(Type, Name)
```

### C#

```csharp
System.bool IsNameUsed(
   System.int Type,
   System.string Name
)
```

### C++/CLI

```cpp
System.bool IsNameUsed(
   System.int Type,
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of entity or entities whose names to check as defined by [swNameType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNameType_e.html)
- `Name`: Name of entity

### Return Value

True if name is in use (i.e., not valid to use again); false if the name is not in use (i.e., valid to use)

## VBA Syntax

See [FeatureManager::IsNameUsed](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~IsNameUsed.html).

## Remarks

Call this method before calling [IBody2::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Name.html) to check to see if the new name specified for the selected body is valid.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
