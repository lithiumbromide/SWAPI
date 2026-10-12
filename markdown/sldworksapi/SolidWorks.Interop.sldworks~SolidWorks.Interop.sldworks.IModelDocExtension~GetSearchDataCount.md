---
title: "GetSearchDataCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSearchDataCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.html"
---

# GetSearchDataCount Method (IModelDocExtension)

Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSearchDataCount( _
   ByVal AppName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppName As System.String
Dim value As System.Integer

value = instance.GetSearchDataCount(AppName)
```

### C#

```csharp
System.int GetSearchDataCount(
   System.string AppName
)
```

### C++/CLI

```cpp
System.int GetSearchDataCount(
   System.String^ AppName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppName`: Third-party application name

### Return Value

Number of keywords for AppName previously added to this model document

## VBA Syntax

See [ModelDocExtension::GetSearchDataCount](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetSearchDataCount.html).

## Remarks

Call this method before calling [IModelDocExtension::IGetSearchData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetSearchData.html) to determine the size of the arrays for that method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.html)
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.html)
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
