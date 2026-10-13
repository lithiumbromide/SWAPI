---
title: "DeleteSearchData Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteSearchData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.html"
---

# DeleteSearchData Method (IModelDocExtension)

Deletes the specified SOLIDWORKS Search third-party keywords from the model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteSearchData( _
   ByVal AppName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppName As System.String
Dim value As System.Boolean

value = instance.DeleteSearchData(AppName)
```

### C#

```csharp
System.bool DeleteSearchData(
   System.string AppName
)
```

### C++/CLI

```cpp
System.bool DeleteSearchData(
   System.String^ AppName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppName`: Application name whose keywords to delete

### Return Value

True if the keywords for AppName are deleted, false if not

## VBA Syntax

See [ModelDocExtension::DeleteSearchData](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~DeleteSearchData.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.html)
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.html)
[IModelDocExtension::GetSearchDataCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.html)
[IModelDocExtension::IGetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
