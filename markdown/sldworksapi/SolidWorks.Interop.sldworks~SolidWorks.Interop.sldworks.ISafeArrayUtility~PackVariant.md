---
title: "PackVariant Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PackVariant"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PackVariant.html"
---

# PackVariant Method (ISafeArrayUtility)

Packs the specified native SOLIDWORKS Dispatch-based objects of the same data type into a Variant SafeArray and returns that packed Variant SafeArray to use in methods requiring passing a packed Variant SafeArray.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PackVariant( _
   ByRef VariantArray As System.Object, _
   ByVal Count As System.Integer, _
   ByVal Type As System.Integer, _
   ByRef Data As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Count As System.Integer
Dim Type As System.Integer
Dim Data As System.Integer

instance.PackVariant(VariantArray, Count, Type, Data)
```

### C#

```csharp
void PackVariant(
   out System.object VariantArray,
   System.int Count,
   System.int Type,
   ref System.int Data
)
```

### C++/CLI

```cpp
void PackVariant(
   [Out] System.Object^ VariantArray,
   System.int Count,
   System.int Type,
   System.int% Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Packed Variant SafeArray
- `Count`: Number of native SOLIDWORKS Dispatch-based objects of Type
- `Type`: Data type as defined in [swSafeArrayType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSafeArrayType_e.html)
- `Data`: Native SOLIDWORKS Dispatch-based objects of Type

## Examples

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetInfo.html)
[ISafeArrayUtility::UnPackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~UnPackVariant.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
