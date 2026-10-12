---
title: "GetFirstFavoriteResult Method (IEdmSearch10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch10"
member: "GetFirstFavoriteResult"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10~GetFirstFavoriteResult.html"
---

# GetFirstFavoriteResult Method (IEdmSearch10)

Gets the first file or folder that matches the favorite search criteria.

## Syntax

### Visual Basic

```vb
Function GetFirstFavoriteResult( _
   ByVal bsFavName As System.String, _
   Optional ByVal bGetCustomColumns As System.Boolean _
) As IEdmSearchResult5
```

### C#

```csharp
IEdmSearchResult5 GetFirstFavoriteResult(
   System.string bsFavName,
   System.bool bGetCustomColumns
)
```

### C++/CLI

```cpp
IEdmSearchResult5^ GetFirstFavoriteResult(
   System.String^ bsFavName,
   System.bool bGetCustomColumns
)
```

### Parameters

- `bsFavName`: Name of a favorite search
- `bGetCustomColumns`: True to retrieve custom column information, false to not

### Return Value

[IEdmSearchResult5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html)

## Examples

See the [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html) examples.

## Remarks

If bGetCustomColumns is set to true and custom columns exist in the search results of bsFavName, then use [IEdmSearchResult6::GetCustomColumnsInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnsInfo.html) and [IEdmSearchResult6::GetCustomColumnValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnValues.html) to see the custom column information.

After calling this method, call [IEdmSearch5::GetNextResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetNextResult.html) repeatedly to retrieve the rest of the search results.

## See Also

[IEdmSearch10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html)
[IEdmSearch10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10_members.html)

## Availability

SOLIDWORKS PDM Professional 2021
