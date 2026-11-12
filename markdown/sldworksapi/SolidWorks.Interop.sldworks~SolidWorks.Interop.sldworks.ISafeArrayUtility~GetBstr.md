---
title: "GetBstr Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetBstr"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBstr.html"
---

# GetBstr Method (ISafeArrayUtility)

Gets the specified BSTR in a Variant SafeArray of BSTRs.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBstr( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.String

value = instance.GetBstr(VariantArray, Index)
```

### C#

```csharp
System.string GetBstr(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetBstr(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of BSTRs
- `Index`: Index of BSTR

### Return Value

BSTR

## Examples

[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

## Remarks

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutBstr Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBstr.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
