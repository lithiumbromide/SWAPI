---
title: "SuppressUnsuppressContactPair2 Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "SuppressUnsuppressContactPair2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SuppressUnsuppressContactPair2.html"
---

# SuppressUnsuppressContactPair2 Method (ICWContactManager)

Sets the suppression state of the specified contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Function SuppressUnsuppressContactPair2( _
   ByVal SName As System.String, _
   ByVal BSuppress As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim SName As System.String
Dim BSuppress As System.Boolean
Dim value As System.Integer

value = instance.SuppressUnsuppressContactPair2(SName, BSuppress)
```

### C#

```csharp
System.int SuppressUnsuppressContactPair2(
   System.string SName,
   System.bool BSuppress
)
```

### C++/CLI

```cpp
System.int SuppressUnsuppressContactPair2(
   System.String^ SName,
   System.bool BSuppress
)
```

### Parameters

- `SName`: Name of contact set (see **Remarks**)
- `BSuppress`: -1 or true to suppress, 0 or false to unsuppress

### Return Value

Error code as defined in [swsContactSuppressUnsuppressError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSuppressUnsuppressError_e.html)

## VBA Syntax

See [CWContactManager::SuppressUnsuppressContactPair2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~SuppressUnsuppressContactPair2.html).

## Remarks

Before calling this method, use:

- [ICWContactSet::ContactName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactName.html) to get the name of the contact set.
- [ICWContactSet::State](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~State.html) to get the current suppression state of the contact set.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
