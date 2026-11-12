---
title: "SuppressUnsuppressComponentContact2 Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "SuppressUnsuppressComponentContact2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SuppressUnsuppressComponentContact2.html"
---

# SuppressUnsuppressComponentContact2 Method (ICWContactManager)

Sets the suppression state of the specified component contact.

## Syntax

### Visual Basic (Declaration)

```vb
Function SuppressUnsuppressComponentContact2( _
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

value = instance.SuppressUnsuppressComponentContact2(SName, BSuppress)
```

### C#

```csharp
System.int SuppressUnsuppressComponentContact2(
   System.string SName,
   System.bool BSuppress
)
```

### C++/CLI

```cpp
System.int SuppressUnsuppressComponentContact2(
   System.String^ SName,
   System.bool BSuppress
)
```

### Parameters

- `SName`: Name of component contact (see **Remarks**)
- `BSuppress`: -1 or true to suppress, 0 or false to unsuppress

### Return Value

Error code as defined in [swsContactSuppressUnsuppressError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSuppressUnsuppressError_e.html)

## VBA Syntax

See [CWContactManager::SuppressUnsuppressComponentContact2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~SuppressUnsuppressComponentContact2.html).

## Remarks

Before calling this method, use:

- [ICWContactComponent::ContactName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactName.html) to get the name of the component contact.
- [ICWContactComponent:State](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~State.html) to get the current suppression state of the component contact.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
