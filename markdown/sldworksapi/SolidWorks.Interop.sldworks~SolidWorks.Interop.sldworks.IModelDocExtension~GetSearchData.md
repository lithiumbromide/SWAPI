---
title: "GetSearchData Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSearchData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.html"
---

# GetSearchData Method (IModelDocExtension)

Gets the SOLIDWORKS Search, third-party, application keywords from the model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSearchData( _
   ByVal AppName As System.String, _
   ByRef AppNames As System.Object, _
   ByRef NodeNames As System.Object, _
   ByRef NodeValues As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppName As System.String
Dim AppNames As System.Object
Dim NodeNames As System.Object
Dim NodeValues As System.Object
Dim value As System.Integer

value = instance.GetSearchData(AppName, AppNames, NodeNames, NodeValues)
```

### C#

```csharp
System.int GetSearchData(
   System.string AppName,
   out System.object AppNames,
   out System.object NodeNames,
   out System.object NodeValues
)
```

### C++/CLI

```cpp
System.int GetSearchData(
   System.String^ AppName,
   [Out] System.Object^ AppNames,
   [Out] System.Object^ NodeNames,
   [Out] System.Object^ NodeValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppName`: Third-party application name whose keywords to get
- `AppNames`: Array of strings of the third-party application name
- `NodeNames`: Array of strings of the third-party application name's keywords
- `NodeValues`: Array of strings of the third-party application name's keyword values

### Return Value

Number of third-party application name's keywords

## VBA Syntax

See [ModelDocExtension::GetSearchData](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetSearchData.html).

## Examples

[Get SOLIDWORKS Search Third-party Keywords (VBA)](Get_SOLIDWORKS_Search_Third-party_Keywords_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.html)
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.html)
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.html)
[IModelDocExtension::GetSearchDataCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
