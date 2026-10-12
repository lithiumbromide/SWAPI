---
title: "UnPackVariant Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "UnPackVariant"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~UnPackVariant.html"
---

# UnPackVariant Method (ISafeArrayUtility)

Unpacks the specified packed Variant SafeArray to native SOLIDWORKS Dispatch-based objects of the same data type.

## Syntax

### Visual Basic (Declaration)

```vb
Function UnPackVariant( _
   ByVal VariantArray As System.Object, _
   ByVal Count As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Count As System.Integer
Dim value As System.Integer

value = instance.UnPackVariant(VariantArray, Count)
```

### C#

```csharp
System.int UnPackVariant(
   System.object VariantArray,
   System.int Count
)
```

### C++/CLI

```cpp
System.int UnPackVariant(
   System.Object^ VariantArray,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray
- `Count`: Number of native SOLIDWORKS Dispatch-based objects of the same data type

### Return Value

Native SOLIDWORKS Dispatch-based objects of the same data type

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetInfo.html)
[ISafeArrayUtility::PackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PackVariant.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
