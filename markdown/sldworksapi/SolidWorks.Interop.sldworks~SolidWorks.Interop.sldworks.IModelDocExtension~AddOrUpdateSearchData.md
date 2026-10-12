---
title: "AddOrUpdateSearchData Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddOrUpdateSearchData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.html"
---

# AddOrUpdateSearchData Method (IModelDocExtension)

Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddOrUpdateSearchData( _
   ByVal AppName As System.String, _
   ByVal AppKeyword As System.String, _
   ByVal AppValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppName As System.String
Dim AppKeyword As System.String
Dim AppValue As System.String
Dim value As System.Boolean

value = instance.AddOrUpdateSearchData(AppName, AppKeyword, AppValue)
```

### C#

```csharp
System.bool AddOrUpdateSearchData(
   System.string AppName,
   System.string AppKeyword,
   System.string AppValue
)
```

### C++/CLI

```cpp
System.bool AddOrUpdateSearchData(
   System.String^ AppName,
   System.String^ AppKeyword,
   System.String^ AppValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppName`: Third-party application name
- `AppKeyword`: Third-party application keyword
- `AppValue`: Value for AppKeyword

### Return Value

True if the SOLIDWORKS Search, third-party, application keyword and value are added to the model document, false if not

## VBA Syntax

See [ModelDocExtension::AddOrUpdateSearchData](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddOrUpdateSearchData.html).

## Examples

[Add Third-party Application Keywords to SOLIDWORKS Search and Model (VBA)](Add_Third-party_Application_Keywords_to_SOLIDWORKS_Search_and_Model_Example_VB.htm)

## Remarks

After calling this method and after the keyword has been indexed in SOLIDWORKS Search, type the third-party application name, keyword, or keyword value in the SOLIDWORKS Search box and press Enter. Any documents assigned any of these three strings will appear on the Search tab in the Task Pane.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.html)
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.html)
[IModelDocExtension::GetSearchDataCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.html)
[IModelDocExtension::IGetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
