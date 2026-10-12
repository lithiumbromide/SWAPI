---
title: "GetInfo Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetInfo.html"
---

# GetInfo Method (ISafeArrayUtility)

Gets the number of elements in a Variant SafeArray and their data type.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetInfo( _
   ByVal VariantArray As System.Object, _
   ByRef Count As System.Integer, _
   ByRef Type As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Count As System.Integer
Dim Type As System.Integer

instance.GetInfo(VariantArray, Count, Type)
```

### C#

```csharp
void GetInfo(
   System.object VariantArray,
   out System.int Count,
   out System.int Type
)
```

### C++/CLI

```cpp
void GetInfo(
   System.Object^ VariantArray,
   [Out] System.int Count,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray
- `Count`: Number of elements in VariantArray
- `Type`: Data type of elements in VariantArray as defined in [swSafeArrayType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSafeArrayType_e.html)

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PackVariant.html)
[ISafeArrayUtility::UnPackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~UnPackVariant.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
