---
title: "SuppressUnsuppressComponentContact Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "SuppressUnsuppressComponentContact"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SuppressUnsuppressComponentContact.html"
---

# SuppressUnsuppressComponentContact Method (ICWContactManager)

Obsolete. Superseded by [ICWContactManager::SuppressUnsuppressComponentContact2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SuppressUnsuppressComponentContact2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SuppressUnsuppressComponentContact( _
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

value = instance.SuppressUnsuppressComponentContact(SName, BSuppress)
```

### C#

```csharp
System.int SuppressUnsuppressComponentContact(
   System.string SName,
   System.int BSuppress
)
```

### C++/CLI

```cpp
System.int SuppressUnsuppressComponentContact(
   System.String^ SName,
   System.int BSuppress
)
```

### Parameters

- `SName`: Name of component contact (see **Remarks**)
- `BSuppress`: 1 to suppress, 0 to unsuppress (see **Remarks**)

### Return Value

Error code as defined in [swsContactSuppressUnsuppressError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSuppressUnsuppressError_e.html)

## VBA Syntax

See [CWContactManager::SuppressUnsuppressComponentContact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~SuppressUnsuppressComponentContact.html).

## Examples

[Add Component Contacts (VBA)](Add_Component_Contacts_Example_VB.htm)
[Add Component Contacts (VB.NET)](Add_Component_Contacts_Example_VBNET.htm)
[Add Component Contacts (C#)](Add_Component_Contacts_Example_CSharp.htm)

## Remarks

Before calling this method, use:

- [ICWContactComponent::ContactName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactName.html) to get the name of the component contact.
- [ICWContactComponent:State](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~State.html) to get the current suppression state of the component contact.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactComponent::SuppressUnSuppress Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
