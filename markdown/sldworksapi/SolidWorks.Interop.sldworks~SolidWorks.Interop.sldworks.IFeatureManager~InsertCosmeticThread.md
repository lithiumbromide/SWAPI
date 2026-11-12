---
title: "InsertCosmeticThread Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCosmeticThread"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread.html"
---

# InsertCosmeticThread Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertCosmeticThread2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCosmeticThread2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCosmeticThread( _
   ByVal Type As System.Short, _
   ByVal Depth As System.Double, _
   ByVal Length As System.Double, _
   ByVal Note As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Short
Dim Depth As System.Double
Dim Length As System.Double
Dim Note As System.String
Dim value As System.String

value = instance.InsertCosmeticThread(Type, Depth, Length, Note)
```

### C#

```csharp
System.string InsertCosmeticThread(
   System.short Type,
   System.double Depth,
   System.double Length,
   System.string Note
)
```

### C++/CLI

```cpp
System.String^ InsertCosmeticThread(
   System.short Type,
   System.double Depth,
   System.double Length,
   System.String^ Note
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`:
- `Depth`:
- `Length`:
- `Note`:

## VBA Syntax

See [FeatureManager::InsertCosmeticThread](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCosmeticThread.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability
