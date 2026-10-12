---
title: "GetSSOFormattedURL Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetSSOFormattedURL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSSOFormattedURL.html"
---

# GetSSOFormattedURL Method (ISldWorks)

Formats the specified URL for single sign-on.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSSOFormattedURL( _
   ByVal TargetUrl As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TargetUrl As System.String
Dim value As System.String

value = instance.GetSSOFormattedURL(TargetUrl)
```

### C#

```csharp
System.string GetSSOFormattedURL(
   System.string TargetUrl
)
```

### C++/CLI

```cpp
System.String^ GetSSOFormattedURL(
   System.String^ TargetUrl
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TargetUrl`: URL to format

### Return Value

URL formatted for single sign-on

## VBA Syntax

See [SldWorks::GetSSOFormattedURL](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetSSOFormattedURL.html).

## Remarks

Use this method to log into SOLIDWORKS add-ins using the current SOLIDWORKS credentials.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
