---
title: "SuppressUnsuppressContactPair Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "SuppressUnsuppressContactPair"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SuppressUnsuppressContactPair.html"
---

# SuppressUnsuppressContactPair Method (ICWContactManager)

Obsolete. Superseded by [ICWContactManager::SuppressUnsuppressContactPair2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SuppressUnsuppressContactPair2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SuppressUnsuppressContactPair( _
   ByVal SName As System.String, _
   ByVal BSuppress As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim SName As System.String
Dim BSuppress As System.Integer
Dim value As System.Integer

value = instance.SuppressUnsuppressContactPair(SName, BSuppress)
```

### C#

```csharp
System.int SuppressUnsuppressContactPair(
   System.string SName,
   System.int BSuppress
)
```

### C++/CLI

```cpp
System.int SuppressUnsuppressContactPair(
   System.String^ SName,
   System.int BSuppress
)
```

### Parameters

- `SName`: Name of contact set (see **Remarks**)
- `BSuppress`: 1 to suppress, 0 to unsuppress (see **Remarks**)

### Return Value

Error code as defined in [swsContactSuppressUnsuppressError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSuppressUnsuppressError_e.html)

## VBA Syntax

See [CWContactManager::SuppressUnsuppressContactPair](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~SuppressUnsuppressContactPair.html).

## Examples

See the [ICWContactManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html) examples.

## Remarks

Before calling this method, use:

- [ICWContactSet::ContactName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactName.html) to get the name of the contact set.
- [ICWContactSet::State](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~State.html) to get the current suppression state of the contact set.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactSet::SuppressUnSuppress Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
