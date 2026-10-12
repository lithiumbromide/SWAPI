---
title: "IdentifyToSW Method (SwPEManager)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "SwPEManager"
member: "IdentifyToSW"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.SwPEManager~IdentifyToSW.html"
---

# IdentifyToSW Method (SwPEManager)

Sends the specified callback object to the SOLIDWORKS Partner add-in, requesting a license key.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IdentifyToSW( _
   ByVal ClassFactory As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As SwPEManager
Dim ClassFactory As System.Object

instance.IdentifyToSW(ClassFactory)
```

### C#

```csharp
void IdentifyToSW(
   System.object ClassFactory
)
```

### C++/CLI

```cpp
void IdentifyToSW(
   System.Object^ ClassFactory
)
```

### Parameters

- `ClassFactory`: Pointer to the [ISwPEClassFactory](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory.html) dispatch object

## VBA Syntax

See [SwPEManager::IdentifyToSW](ms-its:swpublishedapivb6.chm::/swpublished~SwPEManager~IdentifyToSW.html).

## Remarks

After receiving the ClassFactory dispatch object, the partner add-in calls [ISwPEClassFactory::SetPartnerKey](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory~SetPartnerKey.html) to send SOLIDWORKS a license key. SOLIDWORKS uses the partner key to verify entitlement of the SOLIDWORKS Partner.

## See Also

[SwPEManager Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.SwPEManager.html)
[SwPEManager Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.SwPEManager_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
