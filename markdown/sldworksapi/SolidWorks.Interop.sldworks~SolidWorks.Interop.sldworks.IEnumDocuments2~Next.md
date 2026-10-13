---
title: "Next Method (IEnumDocuments2)"
project: "SOLIDWORKS API Help"
interface: "IEnumDocuments2"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Next.html"
---

# Next Method (IEnumDocuments2)

Gets the next document in the documents enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As ModelDoc2, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDocuments2
Dim Celt As System.Integer
Dim Rgelt As ModelDoc2
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out ModelDoc2 Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] ModelDoc2^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of documents for the documents enumeration
- `Rgelt`: Pointer to an array of [documents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) of size Celt
- `PceltFetched`: Pointer to the number of documents returned from the list; this value can be less than Celt if you ask for more documents than exist, or it can be NULL if no more documents exist.

## VBA Syntax

See [EnumDocuments2::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumDocuments2~Next.html).

## Examples

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)
[Traverse All Open Documents (C++)](Traverse_All_Open_Documents_Example_CPlusPlus_COM.htm)

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDocuments2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.html)
[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
