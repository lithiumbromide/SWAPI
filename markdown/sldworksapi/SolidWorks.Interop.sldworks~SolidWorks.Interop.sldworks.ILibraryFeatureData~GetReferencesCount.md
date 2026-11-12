---
title: "GetReferencesCount Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "GetReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.html"
---

# GetReferencesCount Method (ILibraryFeatureData)

Gets the number of references for the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.Integer

value = instance.GetReferencesCount()
```

### C#

```csharp
System.int GetReferencesCount()
```

### C++/CLI

```cpp
System.int GetReferencesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of references

## VBA Syntax

See [LibraryFeatureData::GetReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~GetReferencesCount.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

Call this method before calling [ILibraryFeatureData::IGetReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILibraryFeatureData~IGetReferences.html).

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.html)
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html)
[ILibraryFeatureData::SetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
