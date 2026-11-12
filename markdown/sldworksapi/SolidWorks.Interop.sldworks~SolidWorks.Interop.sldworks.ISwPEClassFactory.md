---
title: "ISwPEClassFactory Interface"
project: "SOLIDWORKS API Help"
interface: "ISwPEClassFactory"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory.html"
---

# ISwPEClassFactory Interface

Allows access to the callback object used by [ISwPEManager](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwPEManager.html) to send a license key back to SOLIDWORKS for SOLIDWORKS Partner entitlement verification.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwPEClassFactory
```

### Visual Basic (Usage)

```vb
Dim instance As ISwPEClassFactory
```

### C#

```csharp
public interface ISwPEClassFactory
```

### C++/CLI

```cpp
public interface class ISwPEClassFactory
```

## VBA Syntax

See [SwPEClassFactory](ms-its:sldworksapivb6.chm::/sldworks~SwPEClassFactory.html).

## Remarks

This interface provides a callback mechanism in which:

1. SOLIDWORKS requests the partner's key through the add-in by calling [ISwPEManager::IdentifyToSW](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwPEManager~IdentifyToSW.html),
2. The partner add-in sends a license key back to SOLIDWORKS in [ISwPEClassFactory::SetPartnerKey](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory~SetPartnerKey.html), and
3. SOLIDWORKS uses the license key to verify the entitlement of the SOLIDWORKS Partner and returns [ISwPEToken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEToken.html).

See [SOLIDWORKS Partner Program](ms-its:sldworksapiprogguide.chm::/GettingStarted/SolidWorks_Partner_Program_2.htm).

## Accessors

ISwPEManager::IdentifyToSW

## See Also

[ISwPEClassFactory Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
