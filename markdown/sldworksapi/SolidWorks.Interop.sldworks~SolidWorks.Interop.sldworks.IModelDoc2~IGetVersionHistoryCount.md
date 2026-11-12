---
title: "IGetVersionHistoryCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetVersionHistoryCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetVersionHistoryCount.html"
---

# IGetVersionHistoryCount Method (IModelDoc2)

Gets the size of the array required to hold data returend by [IModleDoc2::IVersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IVersionHistory.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVersionHistoryCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.IGetVersionHistoryCount()
```

### C#

```csharp
System.int IGetVersionHistoryCount()
```

### C++/CLI

```cpp
System.int IGetVersionHistoryCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Size of array required for the version history

## VBA Syntax

See [ModelDoc2::IGetVersionHistoryCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetVersionHistoryCount.html).

## Examples

[Document Version History (C++)](Document_Version_History_Example_CPlusPlus_COM.htm)

## Remarks

If the document has not yet been saved, then no version history information exists and this method returns 0.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.html)
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.html)
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
