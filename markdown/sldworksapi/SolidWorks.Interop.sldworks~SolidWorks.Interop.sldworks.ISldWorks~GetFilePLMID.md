---
title: "GetFilePLMID Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetFilePLMID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFilePLMID.html"
---

# GetFilePLMID Method (ISldWorks)

Gets the Product Lifecycle Management (PLM) ID of the specified file stored in 3DEXPERIENCE.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFilePLMID( _
   ByVal FilePath As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePath As System.String
Dim value As System.String

value = instance.GetFilePLMID(FilePath)
```

### C#

```csharp
System.string GetFilePLMID(
   System.string FilePath
)
```

### C++/CLI

```cpp
System.String^ GetFilePLMID(
   System.String^ FilePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`: Name of file

### Return Value

PLM ID

## VBA Syntax

See [SldWorks::GetFilePLMID](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetFilePLMID.html).

## Remarks

This method is valid only for [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 SP03, Revision Number 30.3
