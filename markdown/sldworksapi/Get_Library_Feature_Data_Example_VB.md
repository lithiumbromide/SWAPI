---
title: "Get Library Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Library_Feature_Data_Example_VB.htm"
---

# Get Library Feature Data Example (VBA)

This example shows how to get data about library features in model documents.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open a model document that contains at least one
'    library feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the FeatureManager design tree searching for
'    library features.
' 2. Gets each library feature's data.
' 3. Inspect the Immediate window.
'-------------------------------------------------------------
Option Explicit
```

```
Dim boolstatus As Boolean
Dim swApp As SldWorks.SldWorks
Dim ModelDoc2 As SldWorks.ModelDoc2
Dim Feature As SldWorks.Feature
Dim NextFeature As SldWorks.Feature
Dim LibraryFeatureData As LibraryFeatureData
Dim placementPlaneType As Long
Dim placementPlane As Object
Dim ConfigurationName As String
Dim vConfigs As Variant
Dim vConfigName As Variant
Dim x As Long
Dim LinkToLibraryPart As Boolean
Dim LocatingDimensionsCount As Long
Dim vLocDimName As Variant
Dim vLocDimVal As Variant
Dim i As Long
Dim bOverrideDimVal As Boolean
Dim SizeDimensionsCount As Long
Dim vSizDimName As Variant
Dim vSizDimVal As Variant
Dim ReferencesCount As Long
Dim vRefType As Variant
Dim vRefName As Variant
Dim vRefs As Variant
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set ModelDoc2 = swApp.ActiveDoc
```

```
' Traverse the FeatureManager design tree searching for library features
Set Feature = ModelDoc2.FirstFeature
```

```
While Not Feature Is Nothing
```

```
    'Debug.Print Feature.Name, Feature.GetTypeName
```

```
    ' If feature is a library feature, then get its data; otherwise,
    ' move onto the next feature in the FeatureManager design tree
```

```
    If Feature.GetTypeName = "LibraryFeature" Then
        Debug.Print ""
        Debug.Print Feature.Name, Feature.GetTypeName
        Set LibraryFeatureData = Feature.GetDefinition
        boolstatus = LibraryFeatureData.AccessSelections(ModelDoc2, Nothing)
```

```
        ' Access the selections of the library feature that define it
        Debug.Print "LibraryFeatureData.AccessSelections = " & boolstatus
```

```
        ' Get its placement type
        Set placementPlane = LibraryFeatureData.GetPlacementPlane2(swLibFeatureData_e.swLibFeatureData_PartRespect, placementPlaneType)
        Debug.Print "PlacementPlaneType = " & placementPlaneType
        placementPlane.Select False
```

```
        ' Get the name of the active library feature configuration
        ConfigurationName = LibraryFeatureData.ConfigurationName
        Debug.Print "ConfigurationName = " & ConfigurationName
```

```
        ' Determine if the library feature is linked to
        ' the library feature part
        LinkToLibraryPart = LibraryFeatureData.LinkToLibraryPart
        Debug.Print "LinkToLibraryPart = " & LinkToLibraryPart
```

```
        ' If the library feature part document is open or
        ' if the library feature is linked to the library feature
        ' part document, then get the names of all of the
        ' library feature configurations; if neither,
        ' then only the name of the active library configuration
        ' is returned
        vConfigs = LibraryFeatureData.GetAllConfigurationNames
        Debug.Print "Configuration names :"
```

```
        If Not IsEmpty(vConfigs) Then
            For x = LBound(vConfigs) To UBound(vConfigs)
                Debug.Print "  " & vConfigs(x)
            Next x
        End If
```

```
        ' Get the number of locating dimensions
        LocatingDimensionsCount = LibraryFeatureData.GetDimensionsCount(0)
        Debug.Print "LocatingDimensionsCount = " & LocatingDimensionsCount
```

```
        ' Get the locating dimensions
        vLocDimVal = LibraryFeatureData.GetDimensions(0, vLocDimName)
        Debug.Print "Locating dimensions :"
```

```
        If Not IsEmpty(vLocDimName) Then
            For i = LBound(vLocDimName) To UBound(vLocDimName)
                Debug.Print "  " & vLocDimName(i), vLocDimVal(i)
            Next i
        End If
```

```
        ' Determine if existing dimension values of the library
        ' feature can be overridden
        bOverrideDimVal = LibraryFeatureData.OverrideDimension
        Debug.Print "OverrideDimension = " & bOverrideDimVal
```

```
        ' Get the number of feature dimensions
        SizeDimensionsCount = LibraryFeatureData.GetDimensionsCount(1)
        Debug.Print "SizeDimensionsCount = " & SizeDimensionsCount
```

```
        ' Get the feature dimensions
        vSizDimVal = LibraryFeatureData.GetDimensions(1, vSizDimName)
        Debug.Print "Size dimensions :"
        If Not IsEmpty(vSizDimName) Then
            For i = LBound(vSizDimName) To UBound(vSizDimName)
```

```
                Debug.Print "  " & vSizDimName(i), vSizDimVal(i)
            Next i
        End If
```

```
        ' Get the number of references
        ReferencesCount = LibraryFeatureData.GetReferencesCount
        Debug.Print "GetReferencesCount = " & ReferencesCount
```

```
        ' Get the references
        vRefs = LibraryFeatureData.GetReferences3(swLibFeatureData_e.swLibFeatureData_PartRespect, vRefType, vRefName)
        If Not IsEmpty(vRefType) Then
            Debug.Print "Reference types and names: "
            For i = LBound(vRefType) To UBound(vRefType)
                Debug.Print "  " & vRefType(i) & ", " & vRefName(i)
                vRefs(i).Select False
            Next i
        End If
```

```
        'Release the selections that define the library feature
        LibraryFeatureData.ReleaseSelectionAccess
```

```
    End If
```

```
    ' Get the next feature until there are no more
    Set NextFeature = Feature.GetNextFeature
    Set Feature = Nothing
    Set Feature = NextFeature
    Set NextFeature = Nothing
```

```
Wend
```

```
End Sub
```
