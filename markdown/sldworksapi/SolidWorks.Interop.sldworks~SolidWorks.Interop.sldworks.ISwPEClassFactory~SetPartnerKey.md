---
title: "SetPartnerKey Method (ISwPEClassFactory)"
project: "SOLIDWORKS API Help"
interface: "ISwPEClassFactory"
member: "SetPartnerKey"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory~SetPartnerKey.html"
---

# SetPartnerKey Method (ISwPEClassFactory)

Sets the license key which SOLIDWORKS uses to verify SOLIDWORKS Partner entitlement.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPartnerKey( _
   ByVal StrPartnerEntitlement As System.String, _
   ByRef TokenObject As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwPEClassFactory
Dim StrPartnerEntitlement As System.String
Dim TokenObject As System.Object
Dim value As System.Integer

value = instance.SetPartnerKey(StrPartnerEntitlement, TokenObject)
```

### C#

```csharp
System.int SetPartnerKey(
   System.string StrPartnerEntitlement,
   out System.object TokenObject
)
```

### C++/CLI

```cpp
System.int SetPartnerKey(
   System.String^ StrPartnerEntitlement,
   [Out] System.Object^ TokenObject
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StrPartnerEntitlement`: License key string (see **Remarks**)
- `TokenObject`: [ISwPEToken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEToken.html) (**for** **future use only - see Remarks**)

### Return Value

Return code as defined by [swPartnerEntitlementStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartnerEntitlementStatus_e.html)

## VBA Syntax

See [SwPEClassFactory::SetPartnerKey](ms-its:sldworksapivb6.chm::/sldworks~SwPEClassFactory~SetPartnerKey.html).

## Remarks

When this method is called, SOLIDWORKS compares the registry against these values in the license key specified in StrPartnerEntitlement:

- SOLIDWORKS Partner entitlement
- SOLIDWORKS version
- Add-in name
- Add-in GUID
- Expiration date

See [SOLIDWORKS Partner Program](ms-its:sldworksapiprogguide.chm::/GettingStarted/SolidWorks_Partner_Program_2.htm).

TokenObject is for future use only.

## See Also

[ISwPEClassFactory Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory.html)
[ISwPEClassFactory Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
