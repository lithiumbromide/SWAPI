---
title: "PutBstr Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutBstr"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBstr.html"
---

# PutBstr Method (ISafeArrayUtility)

Adds the specified BSTR to a Variant SafeArray of BSTRs.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutBstr( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.String

instance.PutBstr(VariantArray, Index, Value)
```

### C#

```csharp
void PutBstr(
   out System.object VariantArray,
   System.int Index,
   System.string Value
)
```

### C++/CLI

```cpp
void PutBstr(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of BSTRs
- `Index`: Index of BSTR
- `Value`: BSTR

## Remarks

Be aware that calling ISafeArrayUtility::PutBstr within a loop that inserts a BSTR repeatedly declared on the stack results in an array of pointers to the same BSTR; i.e., all elements of the SafeArray are the same, which is most likely not your intention. For example, you should avoid using code similar to the following:

for (ULONG ulIndex = 0L; ulIndex < ulSize; ulIndex++)
{
CString testString;
testString.Format(_T('Index = %d'), ulIndex);
CComBSTR bstrTemp = testString;
HRESULT hres = iSAUtil->PutBstr(&vPacked, ulIndex, bstrTemp);

bstrArray[ulIndex] = bstrTemp;
}

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetBstr Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBstr.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
