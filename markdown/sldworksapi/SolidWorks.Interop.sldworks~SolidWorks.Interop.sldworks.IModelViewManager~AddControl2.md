---
title: "AddControl2 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "AddControl2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl2.html"
---

# AddControl2 Method (IModelViewManager)

Obsolete. Superseded by [IModelViewManager::AddControl3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~AddControl3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddControl2( _
   ByVal Name As System.String, _
   ByVal ControlName As System.String, _
   ByVal BstrLicKey As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Name As System.String
Dim ControlName As System.String
Dim BstrLicKey As System.String
Dim value As System.Object

value = instance.AddControl2(Name, ControlName, BstrLicKey)
```

### C#

```csharp
System.object AddControl2(
   System.string Name,
   System.string ControlName,
   System.string BstrLicKey
)
```

### C++/CLI

```cpp
System.Object^ AddControl2(
   System.String^ Name,
   System.String^ ControlName,
   System.String^ BstrLicKey
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `ControlName`:
- `BstrLicKey`:

## VBA Syntax

See [ModelViewManager::AddControl2](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~AddControl2.html).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
