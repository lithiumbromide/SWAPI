---
title: "IGetSearchData Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetSearchData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.html"
---

# IGetSearchData Method (IModelDocExtension)

Gets the SOLIDWORKS Search, third-party, application keywords from the model document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetSearchData( _
   ByVal AppName As System.String, _
   ByVal Count As System.Integer, _
   ByRef AppNames As System.String, _
   ByRef NodeNames As System.String, _
   ByRef NodeValues As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppName As System.String
Dim Count As System.Integer
Dim AppNames As System.String
Dim NodeNames As System.String
Dim NodeValues As System.String

instance.IGetSearchData(AppName, Count, AppNames, NodeNames, NodeValues)
```

### C#

```csharp
void IGetSearchData(
   System.string AppName,
   System.int Count,
   out System.string AppNames,
   out System.string NodeNames,
   out System.string NodeValues
)
```

### C++/CLI

```cpp
void IGetSearchData(
   System.String^ AppName,
   System.int Count,
   [Out] System.String^ AppNames,
   [Out] System.String^ NodeNames,
   [Out] System.String^ NodeValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppName`: Third-party application name whose keywords to get
- `Count`: Number of third-party application keywords
- `AppNames`: - in-process, unmanaged C++: Pointer to an array of the third-party application names

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `NodeNames`: - in-process, unmanaged C++: Pointer to an array of the third-party application name's keywords

  VBA, VB.NET, C#, and C++/CLI: Not supported
- `NodeValues`: - in-process, unmanaged C++: Pointer to an array of the third-party application name's keyword values

  VBA, VB.NET, C#, and C++/CLI: Not supported

### Return Value

Number of third-party application name's keywords

## Remarks

Before calling this method, call [IModelDocExtension::GetSearchDataCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetSearchDataCount.html) to get the value of Count.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.html)
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.html)
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
