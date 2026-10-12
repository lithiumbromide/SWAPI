---
title: "ICreateBaseFeature Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateBaseFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBaseFeature.html"
---

# ICreateBaseFeature Method (IBody2)

Creates a base feature for the imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBaseFeature( _
   ByVal BodyIn As Body2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim BodyIn As Body2
Dim value As System.Boolean

value = instance.ICreateBaseFeature(BodyIn)
```

### C#

```csharp
System.bool ICreateBaseFeature(
   Body2 BodyIn
)
```

### C++/CLI

```cpp
System.bool ICreateBaseFeature(
   Body2^ BodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyIn`: [Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) on which to create base feature

### Return Value

True if the base feature was created, false if not

## VBA Syntax

See [Body2::ICreateBaseFeature](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateBaseFeature.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateBaseFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBaseFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
