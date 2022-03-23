"""explain_test_image

Revision ID: 6e1ed83dd46a
Revises: 4c0b3ba3888d
Create Date: 2021-06-18 14:47:06.774708

"""

"""
 OpenVINO DL Workbench
 Migration: Add explainable ai for classification use case

 Copyright (c) 2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6e1ed83dd46a'
down_revision = '4c0b3ba3888d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inference_test_image_jobs', sa.Column('explain', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inference_test_image_jobs', 'explain')
    # ### end Alembic commands ###
