---
title: "Sketch::Autodimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__Autodimension.htm"
---

# Sketch::Autodimension

## Sketch::AutoDimension

This method is obsolete and has been superseded by [Sketch::AutoDimension2](sldworksAPI.chm::/Sketch/Sketch__AutoDimension2.htm).

Description

This method automatically dimensions the sketch.

Syntax (OLE Automation)

status = Sketch.AutoDimension ( entitiesToDimension, horizontalScheme, horizontalPlacement, verticalScheme, verticalPlacement )

| Input: | (long) entitiesToDimension | Entities to dimension as defined in swAutodimEntities_e |
| --- | --- | --- |
| Input: | (long) horizontalScheme | Horizontal dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) horizontalPlacement | Placement relative to the sketch of the horizontal dimensions as defined in swAutodimHorizontalPlacement_e |
| Input: | (long) verticalScheme | Vertical dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) verticalPlacement | Placement relative to the sketch of the vertical dimensions as defined in swAutodimVerticalPlacement_e |
| Output: | (long) status | swAutodimStatusSuccess if the sketch is automatically dimensioned successfully; see swAutodimStatus_e for values for possible failures |

Syntax (COM)

status = Sketch->AutoDimension ( entitiesToDimension, horizontalScheme, horizontalPlacement, verticalScheme, verticalPlacement, &status )

| Input: | (long) entitiesToDimension | Entities to dimension as defined in swAutodimEntities_e |
| --- | --- | --- |
| Input: | (long) horizontalScheme | Horizontal dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) horizontalPlacement | Placement relative to the sketch of the horizontal dimensions as defined in swAutodimHorizontalPlacement_e |
| Input: | (long) verticalScheme | Vertical dimensioning scheme as defined in swAutodimScheme_e |
| Input: | (long) verticalPlacement | Placement relative to the sketch of the vertical dimensions as defined in swAutodimVerticalPlacement_e |
| Output: | (long) status | swAutodimStatusSuccess if the sketch is automatically dimensioned successfully; see swAutodimStatus_e for values for possible failures |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the entitiesToDimension argument takes the value swAutodimEntitiesSelected, then use ModelDocExtension::SelectByID with a mark value of swAutodimMarkEntities to select the sketch entities to dimension.

Select and mark a unique sketch point or vertical sketch line as the datum for the horizontal dimensioning scheme, using swAutodimMarkHorizontalDatum as the mark value. Similarly, select a unique sketch point or horizontal sketch line as the datum for the vertical dimensioning scheme, using swAutodimMarkVerticalDatum as the mark value.
